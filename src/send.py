#!/usr/bin/python
import sys,os,xmpp

msg="Hello World!"
jid="user@domain.tld"
pwd="secret"

recipient="destination@domain.tld"

jid=xmpp.protocol.JID(jid)

cl=xmpp.Client(jid.getDomain(),debug=[])

cl.connect()

cl.auth(jid.getNode(),pwd)

cl.send(xmpp.protocol.Message(recipient,msg))

cl.disconnect()