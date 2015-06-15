from helpers import *

stop()
command(53100) #SWS: goto/select previous marker/region
State.set(record="0",playstop="0",song=getCurrentName());
State.broadcast()