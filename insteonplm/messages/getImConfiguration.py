from .messageBase import MessageBase
from .messageConstants import *

class GetImConfiguration(MessageBase):
    """Insteon Get IM Configuration Message 0x62"""

    def __init__(self, flags, acknak = None):
        self.code = MESSAGE_GET_IM_CONFIGURATION
        self.sendSize = MESSAGE_GET_IM_CONFIGURATION_SIZE
        self.returnSize = MESSAGE_GET_IM_CONFIGURATION_RECEIVED_SIZE
        self.name = 'Insteon Get IM Configuration Message'
        
        self._messageFlags = flags
        self.spare1 = 0x00
        self.spare2 = 0x00
        self._acknak = self._setacknak(acknak)

    @property
    def hex(self):
        return self._messageToHex(self._messageFlags,
                                  self.spare1,
                                  self.spare2,
                                  self._acknak)

    @property
    def bytes(self):
        return binascii.unhexlify(self.hex)

    @property
    def isack(self):
        if (self._acknak is not None and self._acknak == MESSAGE_ACK):
            return True
        else:
            return False

    @property
    def isnak(self):
        if (self._acknak is not None and self._acknak == MESSAGE_NAK):
            return True
        else:
            return False
