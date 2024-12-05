---
title: Prototyp
---



```sql public_tenders
  select
      *
  from public_tenders.public_tenders
```


```sql public_tenders_count
  select
      count(*) as count_tenders
  from public_tenders.public_tenders
```
<BigValue 
  data={public_tenders_count} 
  value=count_tenders
/>

```sql public_tenders_sum
  select
      sum(smluvni_cena_bez_dph_kc) as sum_smluvni_cena_bez_dph_kc
  from public_tenders.public_tenders
```
<BigValue 
  data={public_tenders_sum} 
  value=sum_smluvni_cena_bez_dph_kc
/>

