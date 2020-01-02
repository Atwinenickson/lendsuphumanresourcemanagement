from django.http import HttpResponseRedirect
from django.urls import reverse

from overtime.models import OvertimeApplication


def approve_overtime_application_finally(id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.status = "Approved"
    overtime_application.save()
    return overtime_application


def reject_finally(overtime_application):
    overtime_application.status = "Rejected"
    overtime_application.save()
    return overtime_application


def supervisor_reject(overtime_application):
    overtime_application.supervisor_approval = "Rejected"
    overtime_application.save()
    return overtime_application


def supervisor_approve(overtime_application):
    overtime_application.supervisor_approval = "Approved"
    overtime_application.save()
    return overtime_application


def hr_approve(overtime_application):
    overtime_application.HR_approval = "Approved"
    overtime_application.save()
    return overtime_application


def hr_reject(overtime_application):
    overtime_application.HR_approval = "Rejected"
    overtime_application.save()
    return overtime_application


def hod_reject(overtime_application):
    overtime_application.HOD_approval = 'Rejected'
    overtime_application.save()
    return overtime_application


def cfo_reject(overtime_application):
    overtime_application.cfo_approval = 'Rejected'
    overtime_application.save()
    return overtime_application


def ceo_reject(overtime_application):
    overtime_application.ceo_approval = 'Rejected'
    overtime_application.save()
    return overtime_application


def hod_approve(overtime_application):
    # Get the overtime application
    overtime_application.HOD_approval = 'Approved'
    overtime_application.save()
    return overtime_application


def cfo_approve(overtime_application):
    overtime_application.cfo_approval = 'Approved'
    overtime_application.save()
    return overtime_application


def ceo_approve(overtime_application):
    # Get the overtime application
    overtime_application.ceo_approval = 'Approved'
    overtime_application.status = "Approved"
    overtime_application.save()
    return overtime_application


def amend_overtime_service(request):
    overtime_application_id = request.POST.get('id')
    overtime_application = OvertimeApplication.objects.get(pk=overtime_application_id)
    overtime_application.date = request.POST.get('date')
    overtime_application.start_time = request.POST.get('start_time')
    overtime_application.end_time = request.POST.get('end_time')
    overtime_application.description = request.POST.get('description')
    overtime_application.save()
    return overtime_application


def reject_overtime_application_service(rejecter, overtime_application):
    if rejecter.is_supervisor:
        rejected_overtime_application = supervisor_reject(overtime_application)

    elif rejecter.is_hod:
        rejected_overtime_application = hod_reject(overtime_application)

    elif rejecter.is_hr:
        rejected_overtime_application = hr_reject(overtime_application)

    elif rejecter.is_cfo:
        rejected_overtime_application = cfo_reject(overtime_application)

    elif rejecter.is_ceo:
        rejected_overtime_application = ceo_reject(overtime_application)
    else:
        rejected_overtime_application = None

    return rejected_overtime_application


def approve_overtime_application_service(approver, overtime_application):
    approved_overtime_application = None

    if approver.is_supervisor:
        approved_overtime_application = supervisor_approve(overtime_application)

    if approver.is_hod:
        approved_overtime_application = hod_approve(overtime_application)

    if approver.is_hr:
        approved_overtime_application = hr_approve(overtime_application)

    if approver.is_cfo:
        approved_overtime_application = cfo_approve(overtime_application)

    if approver.is_ceo:
        approved_overtime_application = ceo_approve(overtime_application)

    return approved_overtime_application
