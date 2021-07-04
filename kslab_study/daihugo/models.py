from django.db import models


class GameMaster(models.Model):

class Player():
    playerid = 1
    playerName = "player[00]"
    rank = 0
    battleNum = 1
class Room(models.Model):
    roomid = 1
    roomName = "Room_" + str(roomid)





class Deck():

class Hand():

class Card(models.Model):
    suit = 1
    rank = 1
class Field(models.Model):
    strengthDirection=True
    filedState=0

# Create your models here.
