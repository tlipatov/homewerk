#!/usr/bin/env python

import sys
import requests
import argparse
import validators
import traceback
import hashlib
import json

class BadSec(object):
  def __init__(self):
    return

  # Try request up to 3 times, anything not 200 also counts as fail
  def request(self, url, headers={}):
    for x in range(0, 3):
      try:
        if self.debug:
          print("trying: %s" % x, file=sys.stderr)
        
        # HTTP Get
        r = requests.get(url=url, headers=headers)

        # Test if return code is 200
        if r.status_code != 200:
          msg = "Non 200 response: %s" % r.reason
          if self.debug: print(msg, file=sys.stderr)
          continue
        return r

      except Exception as e:
        msg = "failed to connect: %s" % e
        if self.debug: 
          print("failed try: %s" % x, file=sys.stderr)
          print(msg, file=sys.stderr)
        continue

    # Raise error if we exceeded the 3 fail limit
    raise RuntimeError(msg)

  # Our main run function
  def run(self, argv):
    # Argparse to get URL and make it look clean
    arg_description = "BadSec homewerk"
    p = argparse.ArgumentParser( description=arg_description, prog="badsec")
    p.add_argument('-D', '--debug', dest='debug', action='store_true', help='Enable debug')
    required_args = p.add_argument_group('required arguments')
    required_args.add_argument('-U', '--url', metavar='URL', default="http://localhost:8888",
      help='NOC List Server URL http://host:port')

    # Read args into a dict. This makes it much simpler to reference
    args = vars(p.parse_args())
    self.debug = args['debug']

    # Validate URL format
    if not  validators.url(args["url"]):
      raise RuntimeError("Invalid URL: %s" % (args["url"]))

    # Set endpoint vars
    auth_url = "%s/auth" % (args["url"])
    users_url = "%s/users" % (args["url"])

    # Get auth token
    r = self.request(auth_url)
    auth_token = r.headers["Badsec-Authentication-Token"]
    if self.debug: print( auth_token, file=sys.stderr )
    
    # Checksum
    hash_string = "%s/users" % auth_token
    c = hashlib.sha256(hash_string.encode()).hexdigest()

    # Get users
    r = self.request(users_url, {"X-Request-Checksum":c})
    
    # Print json format list
    print(json.dumps(r.text.splitlines()), file=sys.stdout)

def main(argv=None):
  argv = argv or sys.argv[1:]
  badsec = BadSec()

  # Catch anything we raise downstream
  # Also makes clean error msgs
  try:
    badsec.run(argv)
  except Exception as e:
    if hasattr(badsec, 'debug'):
      if badsec.debug:
        traceback.print_exc(file=sys.stderr)
      else:
        print(e)
    return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
