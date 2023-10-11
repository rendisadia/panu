# Credit @BongoBondhuSheikhMujiburRahman.
# Please Don't remove credit.
# Born to make history @BongoBondhuSheikhMujiburRahman !
# Thank you BongoBondhuSheikhMujiburRahman for helping us in this Journey
# 🥰  Thank you for giving me credit @BongoBondhuSheikhMujiburRahmanr  🥰
# for any error please contact me -> telegram@BongoBondhuSheikhMujiburRahmanr or insta @BongoBondhuSheikhMujiburRahmanr 
# rip paid developers 🤣 - >> No need to buy paid source code while @BongoBondhuSheikhMujiburRahmanr is here 😍😍
def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    """ Returns a human readable string representation of bytes """
    return str(bytes) + units[0] if int(bytes) < 1024 else human_size(int(bytes)>>10, units[1:])
