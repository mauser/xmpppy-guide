#!/usr/bin/python
import sys,os,xmpp

msg="Hello World!"
jid="user@domain.tld"
pwd="secret"

recipient="destination@domain.tld"

jid=xmpp.protocol.JID(jid)

cl=xmpp.Client(jid.getDomain(),debug=[])

if cl.connect() == "":
        print "not connected"
        sys.exit(0)

if cl.auth(jid.getNode(),pwd) == None:
        print "authentication failed"
        sys.exit(0)


cl.send(xmpp.protocol.Message(recipient,msg))

cl.disconnect()
