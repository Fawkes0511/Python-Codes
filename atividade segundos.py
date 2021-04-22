segundos = int(input())

Ad = segundos // 86400
seg_rest = segundos % 86400
Bh = seg_rest // 3600
seg_rest = seg_rest % 3600
Cm = seg_rest // 60
seg_rest = seg_rest % 60

print('{}d {}h {}m {}s'.format(Ad,Bh,Cm,seg_rest))