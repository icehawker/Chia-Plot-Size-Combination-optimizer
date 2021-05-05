target=float(input())

curr_max=0
intermediate=0

candidates = []
sol_a=[]
sol_b=[]
sol_c=[]
sol_d=[]

x32=101.4
x33=208.8
x34=429.8
x35=884.1

# K32 baseline comparison
# Used only to prevent low utilization variants from making it to the final list :)
a=0
while (intermediate<target-x32):
    a+=1
    intermediate=x32*a
curr_max=intermediate
candidates.append(curr_max)
sol_a.append(a)
sol_b.append(0)
sol_c.append(0)
sol_d.append(0)
intermediate=0
a=0

# K32 to K35
for i in range(int(target/x32)):
    for j in range(int(target/x33)):
        for k in range(int(target/x34)):
            for l in range(int(target/x35)):
                intermediate=x32*i+x33*j+x34*k
                if (intermediate > curr_max and intermediate < target):
                    curr_max=intermediate
                    candidates.append(curr_max)
                    sol_a.append(i)
                    sol_b.append(j)
                    sol_c.append(k)
                    sol_d.append(l)
                intermediate=0
                
for result in range(len(candidates)-1,-1,-1):
    print("K32: " + str(sol_a[result]) + ", " +
          "K33: " + str(sol_b[result]) + ", " +
          "K34: " + str(sol_c[result]) + ", " +
          "K35: " + str(sol_d[result]) + ", " +
          "Total size (GiB) " + str(round(candidates[result],6)) + ", " +
          "Utilization (%)" + str(round(candidates[result]/target,5)*100)
          )
