
from django.shortcuts import render,redirect
from django.http import HttpResponse

def input_view(request):
    return render(request,'input.html')

def output_view(request):
    global value1
    global value2
    value1 = int(request.GET['fno'])
    value2 = int(request.GET['sno'])

    btnValue = request.GET['mybtn']

    if btnValue=='Add':
        return redirect(Add_View) #  direct view name

    if btnValue=='Sub':
        return redirect('sub') # aliace urlname

    if btnValue=='Mul':
        return redirect('/mul/') # urlname

def Add_View(request):
    response = "The addition of ", value1, " and ", value2, " is : ", (value1 + value2)
    return HttpResponse(response)


def Sub_View(request):
    response = "The substraction of ", value1, " and ", value2, " is : ", (value1 - value2)
    return HttpResponse(response)

def Mul_View(request):
    response = "The multiplication of ", value1, " and ", value2, " is : ", (value1 * value2)
    return HttpResponse(response)


'''
    if btnValue=='Add':
        response = "The addition of ",value1 ," and ",value2 ," is : " ,(value1 + value2)
        return HttpResponse(response)

    elif btnValue=='Sub':
        response = "The substraction of ",value1 ," and ",value2 ," is : " ,(value1 - value2)
        return HttpResponse(response)
    
    elif btnValue=='Mul':
        response = "The multiplication of ",value1 ," and ",value2 ," is : " ,(value1 * value2)
        return HttpResponse(response)
    
    elif btnValue=='Div':
        response = "The division of ",value1 ," and ",value2 ," is : " ,(value1 / value2)
        return HttpResponse(response)
    
    else:
        return HttpResponse('Something wrong')
'''
