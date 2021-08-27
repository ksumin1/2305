import my_module as mm
mm.지원이()
print(mm.date)

import travel.gangreung as ga
gp = ga.GangreungPackage()
print(gp)


from travel import gangreung
gp = gangreung.GangreungPackage()
print(gp)

from travel.gangreung import GangreungPackage
gp = GangreungPackage()
print(gp)

from travel import ilsan
ilsan.이지()

from travel import*
ilsan.이지()

gp=gangreung.GangreungPackage()
print(gp)