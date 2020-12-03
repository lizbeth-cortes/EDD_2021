from backtracking import LaberintoADT
pasillo_inicial=((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab = LaberintoADT(6,6,pasillo_inicial, (5,2), (2,5))
lab.to_string()
