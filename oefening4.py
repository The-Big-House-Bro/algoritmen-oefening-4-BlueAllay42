def countTargetPairs():
     nums.sort()
        juiste = 0 
        linksegetallen = 0
        rechtsegetallen = len(nums)-1
        while linksegetallen < rechtsegetallen: #zolang het linker getal kleiner is dan het rechter
            if nums[linksegetallen] + nums[rechtsegetallen] < target: #de coordinaten van de getallen moeten kleiner zijn dan het target
                juist = juist + rechtsegetallen - linksegetallen 
                linksegetallen = linksegetallen + 1
            else: 
                rechtsegetallen = rechtsegetallen - 1
        return juiste 