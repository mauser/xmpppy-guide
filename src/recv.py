#!/usr/bin/python
import sys
import xmpp
import os
import signal
import time

def messageCB(conn,msg):
	print "Sender: " + str(msg.getFrom())
	print "Content: " + str(msg.getBody())
	print msg


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
	pwd="secret"

	jid=xmpp.protocol.JID(jid)

	cl = xmpp.Client(jid.getDomain(), debug=['nodebuilder', 'dispatcher', 'gen_auth', 'SASL_auth', 'bind', 'socket',
 'CONNECTproxy', 'TLS', 'roster', 'browser', 'ibb'])

	cl.connect()

	cl.auth(jid,pwd)

	cl.RegisterHandler('message', messageCB)

	cl.sendInitPresence()

	GoOn(cl)

main()


