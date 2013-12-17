# Egg of P'an Ku -- an unofficial client for Legend of the Five Rings
# Copyright (C) 2008  Peter C O Johansson
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
"""User interface identifiers and other constants."""

EOPK_APPNAME = 'Egg of P\'an Ku' 
EOPK_VERSION_MAJOR = 0
EOPK_VERSION_MINOR = 9
EOPK_VERSION_REVISION = 4
EOPK_BETA = '2'
EOPK_VERSION_FULL = '%d.%d.%d%s' % (EOPK_VERSION_MAJOR, EOPK_VERSION_MINOR, EOPK_VERSION_REVISION, EOPK_BETA)
EOPK_VERSION_STRING = EOPK_VERSION_FULL + ' (2014-January-01)'
EOPK_COPYRIGHT = 'Copyright (C) 2014 Ryan Karetas'

EOPK_UNOFFICIAL_TEXT = " -- an unofficial Legend of the Five Rings online tabletop"
EOPK_WARRANTY_TEXT = "comes with ABSOLUTELY NO WARRANTY." \
			" This is free software, and you are welcome to redistribute it" \
			" under certain conditions; see LICENSE for details."

EOPK_WEBSITE_URL = "http://www.google.com"
EOPK_DONATE_URL = "https://www.google.com"

ID_MAIN_WINDOW = 20000
ID_CARD_PREVIEW = 20001
ID_CLIENT_LIST = 20002
ID_IRC_CHAT_ENTRY = 20003

ID_MNU_HOST = 101
ID_MNU_CONNECT = 102
ID_MNU_DISCONNECT = 103
ID_MNU_JOIN_GAME = 104
ID_MNU_CHANGE_DECK = 105
ID_MNU_LEAVE_GAME = 106
ID_MNU_START_GAME = 107
ID_MNU_DECK_EDIT = 108
ID_MNU_EXIT = 109
ID_MNU_PREFERENCES = 110
ID_MNU_FIND_GAME_MATCH = 111
ID_MNU_LAUNCH_EGGUPDATER = 112

ID_MNU_PHASE_NEXT = 200
ID_MNU_PHASE_STRAIGHTEN = 201
ID_MNU_PHASE_EVENTS = 202
ID_MNU_PHASE_ACTION = 203
ID_MNU_PHASE_COMBAT = 204
ID_MNU_PHASE_DYNASTY = 205
ID_MNU_PHASE_CLEANUP = 206
ID_MNU_FAMILY_HONOR_SET = 207
ID_MNU_FAMILY_HONOR_INC = 208
ID_MNU_FAMILY_HONOR_DEC = 209
ID_MNU_TURN_PASS = 210
ID_MNU_COIN_FLIP = 211
ID_MNU_ROLL_DICE = 212
ID_MNU_CREATE_CARD = 213
ID_MNU_STRAIGHTEN_ALL = 214
ID_MNU_TAKE_FAVOR = 215
ID_MNU_DISCARD_FAVOR = 216
ID_MNU_REMOVE_MARKERS = 217

ID_MNU_DYN_SHUFFLE = 300
ID_MNU_DYN_SEARCH = 301
ID_MNU_DYN_LOOK_TOP = 302
ID_MNU_DYN_LOOK_BOTTOM = 303

ID_MNU_FATE_DRAW = 401
ID_MNU_FATE_DRAW_X = 402
ID_MNU_FATE_SHUFFLE = 403
ID_MNU_FATE_SEARCH = 404
ID_MNU_FATE_LOOK_TOP = 405
ID_MNU_FATE_LOOK_BOTTOM = 406

ID_MNU_HAND_REVEAL = 500
ID_MNU_HAND_REVEAL_RANDOM = 501
ID_MNU_HAND_REVEAL_X_RANDOM = 502
ID_MNU_HAND_DISCARD = 503
ID_MNU_HAND_DISCARD_RANDOM = 504

ID_MNU_CREATE_CARD_CUSTOM = 600  # 601-699 are specific ones.

ID_MNU_FOCUS_CREATE = 700

ID_MNU_HELP = 800
ID_MNU_HELP_ABOUT = 801
ID_MNU_HELP_WEB = 802
ID_MNU_HELP_DONATE = 803

ID_LIST_HAND = 1000
ID_TRAY_DISCARD_FATE = 1001
ID_TRAY_DISCARD_DYNASTY = 1002
ID_TRAY_DECK_FATE = 1003
ID_TRAY_DECK_DYNASTY = 1004

ID_MNU_CARDPOPUP_TAP = 2000
ID_MNU_CARDPOPUP_FLIP = 2001
ID_MNU_CARDPOPUP_DISCARD = 2002
ID_MNU_CARDPOPUP_KILL_DISCARD = 2003
ID_MNU_CARDPOPUP_DECK_TOP = 2004
ID_MNU_CARDPOPUP_DECK_BOTTOM = 2005
ID_MNU_CARDPOPUP_PEEK = 2006
ID_MNU_CARDPOPUP_DISHONOR = 2007
ID_MNU_CARDPOPUP_MOVE_TOP = 2008
ID_MNU_CARDPOPUP_MOVE_BOTTOM = 2009
ID_MNU_CARDPOPUP_MARK_DEAD = 2010
ID_MNU_CARDPOPUP_MARK_DISCARDED = 2011

#added 1/5/2009 by PCW
ID_MNU_FOCUSPOPUP_DECK_TOP = 2012
ID_MNU_FOCUSPOPUP_DECK_BOTTOM = 2013

#added 1/6/2009 by PCW
ID_MNU_FATEDECKPOPUP_DECK_TOP = 2014
ID_MNU_FATEDECKPOPUP_DECK_BOTTOM = 2015
ID_MNU_CARDPOPUP_PEEK_OPPONENT = 2016

#PCW added 1/22/09
ID_MNU_CARDPOPUP_MARK_REHONOR = 2017


ID_MNU_CARDPOPUP_TOKEN_ADD_CUSTOM = 2099
ID_MNU_CARDPOPUP_TOKEN_ADD = 2100     # 2100..2199
ID_MNU_CARDPOPUP_TOKEN_REMOVE = 2200  # 2200..2299

ID_MNU_CARDPOPUP_CONTROL = 2300  # 2300..2349

ID_MNU_CARDPOPUP_MARKER_ADD_CUSTOM = 2399
ID_MNU_CARDPOPUP_MARKER_ADD = 2400 #2400...2449
ID_MNU_CARDPOPUP_MARKER_REMOVE = 2450 #2400...2449

ID_MNU_PILEPOPUP_SEARCH = 2500
ID_MNU_PILEPOPUP_SHUFFLE = 2501

ID_MNU_CLIENT_IGNORE = 2510
ID_MNU_CLIENT_DYN_DISCARD = 2511
ID_MNU_CLIENT_FATE_DISCARD = 2512
