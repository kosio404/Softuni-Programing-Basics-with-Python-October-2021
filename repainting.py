protective_nylon=1.5
paint=14.5
paint_thinner=5
nylon_needed=int(input())
paint_needed=int(input())
paint_thinner_needed=int(input())
working_hours=int(input())
backup_paint=paint_needed*0.1
backup_nylon=2
bags=0.4
sum_nyloon=(nylon_needed+backup_nylon)*protective_nylon
sum_paint=(paint_needed+backup_paint)*paint
sum_paint_thinner=paint_thinner_needed*paint_thinner
sum_for_materials=sum_paint+sum_paint_thinner+sum_nyloon+bags
price_for_masters=(sum_for_materials*0.3)*working_hours
final_price=price_for_masters+sum_for_materials
print(sum_nyloon)
print(sum_paint)
print(sum_paint_thinner)
print(sum_for_materials)
print(price_for_masters)
print(final_price)
