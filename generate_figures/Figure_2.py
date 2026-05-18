import matplotlib.pyplot as plt
import numpy as np


# def contact_opportunity_rate(v):
#     global model,theta_u,theta_v

#     if model=='Homogeneous':
#         return (1-v)**2 + 2*v*(1-v)*theta_u + theta_u*theta_v*v**2
#     else:
#         return 1

# def contact_probability(v):
#     global model,theta_u,theta_v
    
#     if model == 'Heterogeneous':
#         return (1-v)**2 + 2*v*(1-v)*theta_u + theta_u*theta_v*v**2
#     else:
#         return 1

def contact_rate(v):
    global model
    return (1-v)**2 + 2*v*(1-v)*theta_u + theta_u*theta_v*v**2

        


def R_eff(v):
    global Psi,theta_u,theta_v
    
    if model == 'Homogeneous':
        return contact_rate(v)*(1-(1-Psi)*v)
    else:

        a=Psi*theta_u*theta_v-1
        b=2*(1+Psi*theta_u*(theta_v-(2*theta_u)))
        c=1+2*Psi*theta_u*(theta_v-theta_u)-(2*Psi-(Psi**2)*(theta_v**2))*(theta_u**2)
        
        return (1/2)*(1+a*v+(1-b*v+c*(v**2))**(1/2))




v_values=[i/100 for i in range(101)]


theta_u_vals={'Concave':3,'Convex':1}
theta_v_vals={'Concave':1,'Convex':3}
Psi_vals={'High effectiveness':0.1,'Low effectiveness':0.5}

# plt.figure()
# plt.plot(v_values,[contact_rate(v) for v in v_values])

# plt.figure()





colour={'Heterogeneous':'orangered','Homogeneous':'lightseagreen'}
style={'Heterogeneous':'--','Homogeneous':'-'}


fig = plt.figure(figsize=(6,8))
gs = fig.add_gridspec(6,2)
plt.subplots_adjust(hspace=0.1,wspace=0.1)

j=0
for shape in ['Concave','Convex']:

    model='Homogeneous'
    theta_u=theta_u_vals[shape]
    theta_v=theta_v_vals[shape]
    ax=fig.add_subplot(gs[0,j])
    plt.plot(v_values,[contact_rate(v) for v in v_values],'k',linewidth=3)
    plt.title(shape)
    plt.ylim([0,3.5])
    plt.yticks([1,2,3]) if j==0 else plt.yticks([])
    plt.ylabel('$\\tilde{C}(V)$',rotation=0,labelpad=15) if j==0 else plt.ylabel(None)
    
    plt.xlim([0,1])
    plt.xticks([])
    i=1
    for vaccine in ['High effectiveness','Low effectiveness']:
        
        ax=fig.add_subplot(gs[i,j])
        
        plt.xticks([])
        plt.yticks([1,2]) if j==0 else plt.yticks([])
        plt.xlim([0,1])
        
        plt.ylabel('$\\tilde{R}_{\\text{eff}}(V)$',rotation=0,labelpad=15) if j==0 else plt.ylabel(None)
        upper_limit=1
        for model in ['Heterogeneous','Homogeneous']:
            
            theta_u=theta_u_vals[shape]
            theta_v=theta_v_vals[shape]
            Psi=Psi_vals[vaccine]
            
            
            plt.plot(v_values,[R_eff(v) for v in v_values],colour[model],linestyle=style[model],label=model)
        
            upper_limit = max([R_eff(v) for v in v_values]) if upper_limit < max([R_eff(v) for v in v_values]) else upper_limit
        
        #plt.ylim([0,upper_limit*1.5])  
        plt.ylim([0,2])
        #plt.yticks([i for i in range(1,int(upper_limit*1.5))]) if j==0 else plt.yticks([])
        plt.yticks([0,1]) if j==0 else plt.yticks([])
        plt.text(-0.75,0.7,vaccine.replace(' ',' vaccine\n')+'\n$1-\Psi='+str(round(1-Psi,1))+'$') if shape=='Concave' else None
        plt.legend(loc=1,fontsize=9,bbox_to_anchor=(-0.1, 0.1)) if vaccine=='Low effectiveness' and shape=='Concave' else None
        
        i=i+1
    plt.xticks([0,0.5,1],[0,50,100])
    
    j=j+1
    
    
    plt.xlabel('% vaccinated (V)')

plt.savefig('New figure.png',format='png',dpi=300,bbox_inches='tight')


'''  




plt.figure()
plt.plot(range(101),R_het,':g',label='Heterogeneous mixing by vaccine status')
plt.plot(range(101),R_hom,'orange',label='Homogeneous mixing')
#plt.ylim([0,2])
plt.xticks(range(0,101,10))
plt.xlabel('% Vaccinated')
plt.title('$\Delta R_{\\text{eff}}$',rotation=0,)
plt.legend(loc=3)
'''