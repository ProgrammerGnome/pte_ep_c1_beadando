try: #ezen belűl még több hibakezelés van, de az üzenetek tartalmai nem ütik egymást
        lista = []
        with open('kajabazis.txt') as f: #beolvasom egy listába a forrásfájlt
                for line in f:
                        lista.append(line.strip())

        kaloriak =[]
        etelek = []
        
        n = 0
        
        while("" in lista) : #eltávolítom a listából a beolvasás során keletkezett szóközöket
                lista.remove('')

        for i in lista: #különválogatom az ételek neveit és kalóriatartalmait
                n += 1
                if n % 2 == 0:
                        kaloriak.append(int(i))
                else:
                        etelek.append(i)

        def ismetles_nelkuli_kombinacio(lst, n): #ezzel az algoritmussal meghatározom az összes lehetőséget...
                if n == 0:
                        return [[]]
                l = []
                for i in range(0, len(lst)):
                        m = lst[i]
                        remLst = lst[i + 1:]
                        for p in ismetles_nelkuli_kombinacio(remLst, n-1):
                                l.append([m]+p)	
                return l

        if __name__=="__main__":
                tarolo = kaloriak
                lista = []
                lista.append(ismetles_nelkuli_kombinacio([x for x in tarolo], 2)) #...majd az eredeti listát felülírva belerakom őket.

                print('''--------------------------------WELCOME-----------------------------------
        Ismertető:
Ez a program a kajabazis.txt fájlból (az étel neveit és kalóriatartalmait tartalmazza az utóbbi szerint növekvő sorrendben) készít Önnek egy olyan kétfogásos menüt, amely nem haladja meg az Ön által kívánt kalórialimitet,
de a lehető legtöbb kalóriát tartalmazza, valamint a menü két étele különbözik egymástól.''')

                sorrend_ellenorzo_n = 0 #ez egy hibakezelés, arra az esetre ha az ételek nem sorrendben vannak a forrásfájlban
                for kaloria in kaloriak:
                        sorrend_ellenorzo_n += 1
                        if kaloriak[sorrend_ellenorzo_n-1] > kaloriak[sorrend_ellenorzo_n]:
                                print("\nERROR#0: Kérem növekvő kalóriasorrendben adja meg az ételeket a kajabazis.txt fájlban.")
                                hiba
                        else: break
                        
                try: #hibakezelés rossz formátumú adat megadása esetén
                        limit = int(input("\nKérem adja meg a felső kalórialimitet: "))
                except:
                        print("ERROR#1: Formátumhiba (kérem integert adjon meg).")

                maxi = lista[0][0][0] 
                mini = lista[0][0][0]
                for i in lista: #majd itt fogom kiválogatni az összes lehetőségből a megfelelőket:
                        for j in i: #megfelelő ami a legnagyobb, de a limitnél kisebb.
                                if j[0]+j[1] > maxi and j[0]+j[1] <= limit: #(maximumkiválasztás feltétellel)
                                        maxi = j[0]+j[1]
                                        maxi_1_resze = j[0]
                                        maxi_2_resze = j[1]
                
                sz = 0 #elhelyezkedés (index) alapján visszakeresem az ételek neveit egy másik (de azonos elemszámú) listában
                for i in kaloriak:
                        sz += 1
                        if i == maxi_1_resze:
                                elso_fogas = etelek[sz-1]
                        elif i == maxi_2_resze:
                                masodik_fogas = etelek[sz-1]

                fileobject = open("kimenet.txt", "w")


        class Adatok_kiirasa: #ősosztály az adatok kiírásának előkészítésére

                def __init__(self,elso_szoveg, masodik_szoveg):
                        self.elso_szoveg_1 = elso_szoveg
                        self.masodik_szoveg_1 = masodik_szoveg

                def printname(self):
                        print(self.elso_szoveg_1, self.masodik_szoveg_1)

        class Fajlba_iras_alap_informaciok(Adatok_kiirasa): 
                pass 

        class Fajlba_iras_alap_informaciok: #alosztály ami az alapvető információkat a kimeneti fájlba írja...

                from enum import Enum #...ehhez Enum-ot is hívok segítségül.
                class Szoveg(Enum):
                        kimeneti_szoveg = "A legtöbb kalóriát tartalmazó kettős fogás az adatbázisunkban lévő kaják közül, \nami még nem haladja meg a kalóriabevitel felső limitét. \n(Természetesen a menü itt két különzöző kaját tartalmaz): \n"
                        kimeneti_szoveg_3 = "\n"
                        kimeneti_szoveg_2 = " és "
                        
                        fileobject = open("kimenet.txt", "w")

                        def fgv(kiirando_szoveg): #függvény ami vmit fájlba ír karakterenként
                                for karakter in kiirando_szoveg:
                                        fileobject.write(karakter)

                        def fgv2(fgv, kiirando): #2. függvény aminek a paraméterével meglehet mondani, hogy a "fgv" mit írjon fájlba...
                                fgv(kiirando) 

                        fgv2(fgv, kimeneti_szoveg) #az Enum-okhoz tartozó szövegeket írom fájlba (ezek statikus "adatok")...
                        fgv2(fgv, kimeneti_szoveg_3) #... a változó adatokra változót használok paraméternek:
                        fgv2(fgv, elso_fogas) #pl. itt...
                        fgv2(fgv, kimeneti_szoveg_2)
                        fgv2(fgv, masodik_fogas) #...meg itt is.

        class Egyeb_informaciok_fajlba_es_konzolra(Adatok_kiirasa):
                pass 

        class Egyeb_informaciok_fajlba_es_konzolra: #a második alosztályal pedig másmilyen (szerkezetű és témájú) adatokat írok fájlba

                fileobject.write('\n\nEz a menü ' ) 
                fileobject.write(str(maxi))
                fileobject.write(' kcal-t tartalmaz,') 

                fileobject.write(' az Ön kalórialimite pedig ' ) 
                fileobject.write(str(limit))
                fileobject.write(' kcal volt.') 
                fileobject.close()

                x = Egyeb_informaciok_fajlba_es_konzolra("Sikeresen fájlba íruk az Ön menüjét:","(kimenet.txt).")
                x.printname() #itt használom ki az ősosztály funkcióit is.
except:
        print("ERROR#2: Nem állítható elő menü az adatbázisból.\nAdjon meg magsabb kalórialimitet, vagy ellenőrizze a forrásfájl szerkezetét.")
        
app_vege = input("\n\nNyomjon entert a program bezárásához...") #windows cmd esetére
