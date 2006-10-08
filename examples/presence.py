#!/usr/bin/python
import sys
import xmpp
import os
import signal
import time

def presenceCB(conn,msg):
	print str(msg)
	prs_type=msg.getType()
	who=msg.getFrom()
	if prs_type == "subscribe":
		conn.send(xmpp.Presence(to=who, typ = 'subscribed'))
		conn.send(xmpp.Presence(to=who, typ = 'subscribe'))


def StepOn(conn):
    try:
        conn.Process(1)
    except KeyboardInterrupt:
	    return 0
    return 1

def GoOn(conn):
    while StepOn(conn):
	    pass


def main():
	jid="user@domain.tld"
	pwd="sectret"

	jid=xmpp.protocol.JID(jid)

	cl = xmpp.Client(jid.getDomain(), debug=[])

	cl.connect()

	cl.auth(jid.getNode(),pwd)


	cl.RegisterHandler('presence', presenceCB)
	cl.sendInitPresence()

	GoOn(cl)

main()