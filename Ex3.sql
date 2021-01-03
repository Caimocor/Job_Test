SELECT data, produto, AvgQuantity, WeightedAvg FROM 
			(
              SELECT *, Sum([quantidade]*[preço]) / Sum([quantidade]) as WeightedAvg, Sum([quantidade]) as AvgQuantity
			FROM (
                  SELECT *, 
                      CASE WHEN quantidade > 0 THEN 'BUY'
                              ELSE 'SELL'
                              END AS Type
                   From Trades)
            GROUP BY [data],[Type]
           
           )
ORDER BY data DESC;
