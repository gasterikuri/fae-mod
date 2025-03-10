

init -100 python:

    import os

    def look_for_gift():
        
        gift_path = renpy.config.basedir

        if renpy.exists(gift_path + "/gifts/cookies.gift"):
            
            store.fae_utilities.removeFileDir("{0}/gifts/cookies.gift".format(renpy.config.basedir))

            renpy.call("fae_cookies")
        
        if renpy.exists(gift_path + "/gifts/otter.gift"):

            store.fae_utilities.removeFileDir(gift_path + "/gifts/otter.gift")

            renpy.call("fae_otter")


        else:
            renpy.call("fae_no_gift")
        
        return

label fae_cookies:

    $ store.fae_gifts.cookies = True

    $ refresh()

    #$ store.fae_sprites._auto_gen("abhfaaa")

    s abhfaaa "I found cookies!"

    s "Yum!"

    return

label fae_otter:

    $ store.fae_gifts.otter = True

    $ refresh()

    s "I found an otter!"

    s "She's so cute!"

    return

label fae_chibi:

    if store.fae_gifts.cookies:

        $ store.fae_gifts.cookies = False

        $ store.fae_gifts.chibi = True
    
    else:
        $ store.fae_gifts.chibi = True
    
    $ store.fae_sprites._auto_gen("abhfaaa")
    
    s "Awwww"
    s "She's so cute!"

    return

label fae_no_gift:

    s "I didn't find anything!"

    return


init -100 python in fae_gifts:

    import store

    FAE_GIFT_ZORDER = 5

    cookies = False

    otter = False

    chibi = False

    

