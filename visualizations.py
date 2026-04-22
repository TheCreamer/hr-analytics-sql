import matplotlib.pyplot as plt

def plot_attrition_by_department(data):
    departments = [row[0] for row in data]
    attrition_rates = [row[3] for row in data]

    plt.figure (figsize =(8,5)) 
    plt.bar(departments, attrition_rates, color=['#e74c3c', '#e67e22', '#3498db'])
    plt.title(' Attrition Rate by Department')
    plt.xlabel('Department')
    plt.ylabel('Attrition Rate (%)')
    plt.tight_layout()
    plt.savefig('output/attrition_by_deparment.png')
    plt.close() 
    print("Chart saved: attrition_by_department")

def plot_overtime_attrition(data):
    labels = [row[0] for row in data]
    rates = [row[3] for row in data]

    plt.figure(figsize=(6,5))
    plt.bar(labels, rates, color=['#e74c3c', '#2ecc71'])
    plt.title('Attrition Rate: Overtime vs No Overtime')
    plt.xlabel('Overtime')
    plt.ylabel( 'Attrition Rate (%)')
    plt.tight_layout()
    plt.savefig('output/overtime_attrition.png')
    plt.close()
    print("Chart saved: overtime_attrition.png")

def plot_attrition_by_age(data):
    age_group = [row[0] for row in data]
    rates = [row[3] for row in data]

    plt.figure(figsize=(8,5))
    plt.bar(age_group, rates, color='#9b59b6')
    plt.title('Attrition Rate by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Attrtion Rate (%)')
    plt.tight_layout()
    plt.savefig('output/attrition_by_age.png')
    plt.close()
    print("Chart saved: attrition_by_age.png")

def plot_top_roles(data):
    roles = [row[0] for row in data]
    rates = [row[3] for row in data]

    plt.figure(figsize=(10,5))
    plt.barh(roles,rates, color="#22aee6")
    plt.title('Top 5 Job Roles by Attrition Rate')
    plt.xlabel('Attrtion Rate(%)')
    plt.tight_layout()
    plt.savefig('output/top_roles_attrition.png')
    plt.close()
    print("Chart saved: top_roles_attrition.png")