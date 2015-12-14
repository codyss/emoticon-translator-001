def prime(num)
  if num == 2 || num == 3
    return true
  else
    t = 2
    while t <= num / 2
      if num % t == 0
        return false
        break
      else
        t += 1
      end
    end
    return true
  end
end
