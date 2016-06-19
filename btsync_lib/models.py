class Model(dict):
    def __init__(self, **params):
        assert hasattr(self, 'FIELDS'), "Must define FIELDS"

        for field, factory in self.FIELDS:
            if field in params:
                value = params.pop(field)
                self[field] = factory(value)

        assert len(params) == 0, "Unrecognized params: %r" % params.keys()


class Settings(Model):
    FIELDS = (
        ('dlrate', int),
        ('devicename', str),
        ('ulrate', int),
        ('portmapping', int),
        ('listeningport', int),
        ('defaultsynclevel',int),
        ('silent_update',int),
        ('debug_logging',int),
        ('show_copy_key',int),
        ('show_notifications',int),
        ('autostart',int),
        ('check_update',int),
        ('display_new_version',int)
    )


class Peer(Model):
    FIELDS = (
        ('direct', int),
        ('name', str),
        ('status', str),
        ('downdiff', int),
        ('isonline',int),
        ('lastsynctime',int),
        ('userid',str),
        ('lastseentime',int),
        ('lastsenttime',int),
        ('lastreceivedtime',int),
        ('upfiles',int),
        ('id',str),
        ('updiff',int),
        ('downfiles',int)
    )


class Folder(Model):
    FIELDS = (
        ('name', str),
        ('iswritable', int),
        ('secret', str),
        ('readonlysecret', str),
        ('size', str),
        ('peers', lambda peers: [Peer(**peer) for peer in peers]),
        ('readonlysecret', str),
        ('secrettype', int),
        ('files', int),
        ('status', str),
        ('last_modified', str),
        ('indexing', bool),
        ('has_key', bool),
        ('error', str),
        ('date_added', str),
        ('up_eta', int),
        ('paused', int),
        ('up_status', int),
        ('down_eta', int),
        ('archive', str),
        ('total_size', int),
        ('archive_size', int),
        ('up_speed', int),
        ('synclevel', int),
        ('canencrypt', int),
        ('folderid', int),
        ('down_status', int),
        ('down_speed', int),
        ('path', str),
        ('ismanaged', int),
        ('archive_files', int),
        ('stopped', int),
        ('available_space', int),
        ('encryptedsecret', str)
    )


class FolderPreference(Model):
    FIELDS = (
        ('deletetotrash', int),
        ("iswritable", int),
        ("readonlysecret", str),
        ("relay", int),
        ("searchdht", int),
        ("searchlan", int),
        ("usehosts", int),
        ("usetracker", int),
        ('selectivesync',int),
        ('paused',int),
        ('canencrypt',int),
        ('stopped',int),
        ('secrettype',int)
    )
