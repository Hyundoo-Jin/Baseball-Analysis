# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allstarfull(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    gamenum = models.IntegerField(db_column='gameNum', blank=True, null=True)  # Field name made lowercase.
    gameid = models.CharField(db_column='gameID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gp = models.IntegerField(db_column='GP', blank=True, null=True)  # Field name made lowercase.
    startingpos = models.CharField(db_column='startingPos', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllstarFull'


class Appearances(models.Model):
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g_all = models.IntegerField(db_column='G_all', blank=True, null=True)  # Field name made lowercase.
    gs = models.CharField(db_column='GS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g_batting = models.IntegerField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    g_defense = models.IntegerField(db_column='G_defense', blank=True, null=True)  # Field name made lowercase.
    g_p = models.IntegerField(db_column='G_p', blank=True, null=True)  # Field name made lowercase.
    g_c = models.IntegerField(db_column='G_c', blank=True, null=True)  # Field name made lowercase.
    g_1b = models.IntegerField(db_column='G_1b', blank=True, null=True)  # Field name made lowercase.
    g_2b = models.IntegerField(db_column='G_2b', blank=True, null=True)  # Field name made lowercase.
    g_3b = models.IntegerField(db_column='G_3b', blank=True, null=True)  # Field name made lowercase.
    g_ss = models.IntegerField(db_column='G_ss', blank=True, null=True)  # Field name made lowercase.
    g_lf = models.IntegerField(db_column='G_lf', blank=True, null=True)  # Field name made lowercase.
    g_cf = models.IntegerField(db_column='G_cf', blank=True, null=True)  # Field name made lowercase.
    g_rf = models.IntegerField(db_column='G_rf', blank=True, null=True)  # Field name made lowercase.
    g_of = models.IntegerField(db_column='G_of', blank=True, null=True)  # Field name made lowercase.
    g_dh = models.CharField(db_column='G_dh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g_ph = models.CharField(db_column='G_ph', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g_pr = models.CharField(db_column='G_pr', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Appearances'


class Awardsmanagers(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    awardid = models.CharField(db_column='awardID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tie = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AwardsManagers'


class Awardsplayers(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    awardid = models.CharField(db_column='awardID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tie = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AwardsPlayers'


class Awardssharemanagers(models.Model):
    awardid = models.CharField(db_column='awardID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pointswon = models.IntegerField(db_column='pointsWon', blank=True, null=True)  # Field name made lowercase.
    pointsmax = models.IntegerField(db_column='pointsMax', blank=True, null=True)  # Field name made lowercase.
    votesfirst = models.IntegerField(db_column='votesFirst', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AwardsShareManagers'


class Awardsshareplayers(models.Model):
    awardid = models.CharField(db_column='awardID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pointswon = models.IntegerField(db_column='pointsWon', blank=True, null=True)  # Field name made lowercase.
    pointsmax = models.IntegerField(db_column='pointsMax', blank=True, null=True)  # Field name made lowercase.
    votesfirst = models.IntegerField(db_column='votesFirst', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AwardsSharePlayers'


class Batting(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    stint = models.IntegerField(blank=True, null=True)
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.CharField(db_column='IBB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hbp = models.CharField(db_column='HBP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sh = models.CharField(db_column='SH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sf = models.CharField(db_column='SF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gidp = models.CharField(db_column='GIDP', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Batting'


class Battingpost(models.Model):
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    round = models.CharField(max_length=255, blank=True, null=True)
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.CharField(db_column='CS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.CharField(db_column='HBP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sh = models.CharField(db_column='SH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sf = models.CharField(db_column='SF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gidp = models.CharField(db_column='GIDP', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BattingPost'


class Collegeplaying(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schoolid = models.CharField(db_column='schoolID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CollegePlaying'


class Fielding(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    stint = models.IntegerField(blank=True, null=True)
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.CharField(db_column='GS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    innouts = models.CharField(db_column='InnOuts', max_length=255, blank=True, null=True)  # Field name made lowercase.
    po = models.IntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.CharField(db_column='PB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wp = models.CharField(db_column='WP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sb = models.CharField(db_column='SB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cs = models.CharField(db_column='CS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zr = models.CharField(db_column='ZR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fielding'


class Fieldingof(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    stint = models.IntegerField(blank=True, null=True)
    glf = models.IntegerField(db_column='Glf', blank=True, null=True)  # Field name made lowercase.
    gcf = models.IntegerField(db_column='Gcf', blank=True, null=True)  # Field name made lowercase.
    grf = models.IntegerField(db_column='Grf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldingOF'


class Fieldingofsplit(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    stint = models.IntegerField(blank=True, null=True)
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.IntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.IntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.CharField(db_column='PB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wp = models.CharField(db_column='WP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sb = models.CharField(db_column='SB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cs = models.CharField(db_column='CS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zr = models.CharField(db_column='ZR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldingOFsplit'


class Fieldingpost(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    round = models.CharField(max_length=255, blank=True, null=True)
    pos = models.CharField(db_column='POS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.IntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.IntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    tp = models.IntegerField(db_column='TP', blank=True, null=True)  # Field name made lowercase.
    pb = models.CharField(db_column='PB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sb = models.CharField(db_column='SB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cs = models.CharField(db_column='CS', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldingPost'


class Halloffame(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(blank=True, null=True)
    votedby = models.CharField(db_column='votedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ballots = models.IntegerField(blank=True, null=True)
    needed = models.IntegerField(blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    inducted = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    needed_note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HallOfFame'


class Homegames(models.Model):
    year_key = models.IntegerField(db_column='year.key', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    league_key = models.CharField(db_column='league.key', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    team_key = models.CharField(db_column='team.key', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    park_key = models.CharField(db_column='park.key', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    span_first = models.CharField(db_column='span.first', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    span_last = models.CharField(db_column='span.last', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    games = models.IntegerField(blank=True, null=True)
    openings = models.IntegerField(blank=True, null=True)
    attendance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HomeGames'


class Managers(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inseason = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(blank=True, null=True)
    plyrmgr = models.CharField(db_column='plyrMgr', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Managers'


class Managershalf(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inseason = models.IntegerField(blank=True, null=True)
    half = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ManagersHalf'


class Master(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthyear = models.IntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    birthmonth = models.IntegerField(db_column='birthMonth', blank=True, null=True)  # Field name made lowercase.
    birthday = models.IntegerField(db_column='birthDay', blank=True, null=True)  # Field name made lowercase.
    birthcountry = models.CharField(db_column='birthCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthstate = models.CharField(db_column='birthState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthcity = models.CharField(db_column='birthCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deathyear = models.CharField(db_column='deathYear', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deathmonth = models.CharField(db_column='deathMonth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deathday = models.CharField(db_column='deathDay', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deathcountry = models.CharField(db_column='deathCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deathstate = models.CharField(db_column='deathState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deathcity = models.CharField(db_column='deathCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    namefirst = models.CharField(db_column='nameFirst', max_length=255, blank=True, null=True)  # Field name made lowercase.
    namelast = models.CharField(db_column='nameLast', max_length=255, blank=True, null=True)  # Field name made lowercase.
    namegiven = models.CharField(db_column='nameGiven', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    bats = models.CharField(max_length=255, blank=True, null=True)
    throws = models.CharField(max_length=255, blank=True, null=True)
    debut = models.CharField(max_length=255, blank=True, null=True)
    finalgame = models.CharField(db_column='finalGame', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retroid = models.CharField(db_column='retroID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bbrefid = models.CharField(db_column='bbrefID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Master'


class Parks(models.Model):
    park_key = models.CharField(db_column='park.key', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    park_name = models.CharField(db_column='park.name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    park_alias = models.CharField(db_column='park.alias', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Parks'


class Pitching(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    stint = models.IntegerField(blank=True, null=True)
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.CharField(db_column='BAOpp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    ibb = models.CharField(db_column='IBB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wp = models.CharField(db_column='WP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hbp = models.CharField(db_column='HBP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.CharField(db_column='BFP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gf = models.CharField(db_column='GF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.CharField(db_column='SH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sf = models.CharField(db_column='SF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gidp = models.CharField(db_column='GIDP', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pitching'


class Pitchingpost(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    round = models.CharField(max_length=255, blank=True, null=True)
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.FloatField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase.
    era = models.CharField(db_column='ERA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.IntegerField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.IntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PitchingPost'


class Salaries(models.Model):
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Salaries'


class Schools(models.Model):
    schoolid = models.CharField(db_column='schoolID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name_full = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Schools'


class Seriespost(models.Model):
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    round = models.CharField(max_length=255, blank=True, null=True)
    teamidwinner = models.CharField(db_column='teamIDwinner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgidwinner = models.CharField(db_column='lgIDwinner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    teamidloser = models.CharField(db_column='teamIDloser', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgidloser = models.CharField(db_column='lgIDloser', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SeriesPost'


class Teams(models.Model):
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    franchid = models.CharField(db_column='franchID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    divid = models.CharField(db_column='divID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ghome = models.CharField(db_column='Ghome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    divwin = models.CharField(db_column='DivWin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wcwin = models.CharField(db_column='WCWin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgwin = models.CharField(db_column='LgWin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wswin = models.CharField(db_column='WSWin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.CharField(db_column='CS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hbp = models.CharField(db_column='HBP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sf = models.CharField(db_column='SF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    ha = models.IntegerField(db_column='HA', blank=True, null=True)  # Field name made lowercase.
    hra = models.IntegerField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    bba = models.IntegerField(db_column='BBA', blank=True, null=True)  # Field name made lowercase.
    soa = models.IntegerField(db_column='SOA', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.CharField(db_column='DP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fp = models.FloatField(db_column='FP', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    park = models.CharField(max_length=255, blank=True, null=True)
    attendance = models.CharField(max_length=255, blank=True, null=True)
    bpf = models.IntegerField(db_column='BPF', blank=True, null=True)  # Field name made lowercase.
    ppf = models.IntegerField(db_column='PPF', blank=True, null=True)  # Field name made lowercase.
    teamidbr = models.CharField(db_column='teamIDBR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    teamidlahman45 = models.CharField(db_column='teamIDlahman45', max_length=255, blank=True, null=True)  # Field name made lowercase.
    teamidretro = models.CharField(db_column='teamIDretro', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teams'


class Teamsfranchises(models.Model):
    franchid = models.CharField(db_column='franchID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    franchname = models.CharField(db_column='franchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(max_length=255, blank=True, null=True)
    naassoc = models.CharField(db_column='NAassoc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeamsFranchises'


class Teamshalf(models.Model):
    yearid = models.IntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    half = models.IntegerField(db_column='Half', blank=True, null=True)  # Field name made lowercase.
    divid = models.CharField(db_column='divID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    divwin = models.CharField(db_column='DivWin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeamsHalf'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
