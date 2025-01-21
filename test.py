gender = data.getTheGender() if isLegacyEeInd else data.isWoman() if resolver.resolveObject(Gender, Gender.WOMAN) else resolver.resolveObject(Gender, None)
aboriginal_code = data.getTheAboriginalCode()
is_aboriginal = data.isAbrgInd()
is_visible_minority = data.isDsblInd()
visible_minorities = data.getTheVisibleMinorities()
visible_minority_comment = data.getVisminDetail()
is_disable = data.isDsblInd()
if is_aborginal : 
  print("only variable si_aborginal is data.isDsblInd()")
