import random as r
import termcolor

                                                                        
                           



banner0 = [
    "",
    "  ********                                  *******       **     ********** ",
    " **//////                           **   **/**////**     ****   /////**///  ",
    "/**        **   **  ******  ****** //** ** /**   /**    **//**      /**     ",
    "/*********/**  /** **////  **////   //***  /*******    **  //**     /**     ",
    "////////**/**  /**//***** //*****    /**   /**///**   **********    /**     ",
    "       /**/**  /** /////** /////**   **    /**  //** /**//////**    /**     ",
    " ******** //****** ******  ******   **     /**   //**/**     /**    /**     ",
    "////////   ////// //////  //////   //      //     // //      //     //      ",
    "                                                                            ",
    "                                                                            ",
    "  ********                                                                  ",
    " **//////                                                                   ",
    "/**         *****  ****** **    **  *****  ******                           ",
    "/********* **///**//**//*/**   /** **///**//**//*                           ",
    "////////**/******* /** / //** /** /******* /** /                            ",
    "       /**/**////  /**    //****  /**////  /**                              ",
    " ******** //******/***     //**   //******/***                              ",
    "////////   ////// ///       //     ////// ///                               "
]

colors = ['white','red','light_red','blue','light_blue','cyan']

def printBanner(id=0):
    if id == 0:
        color = colors[r.randrange(len(colors))]
        for i in banner0:
            print(f'{termcolor.colored(i,color,"on_black")}')
            
if __name__ == "__main__":
    printBanner(id=0)
        