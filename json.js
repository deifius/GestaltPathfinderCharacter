var data=[];jQuery("table:eq(1) tbody tr").each(function(n, tr) { data[n]=[]; jQuery(tr).children("td").each(function(nn, td) { data[n][nn]=jQuery(td).text(); }); });JSON.stringify(data);
