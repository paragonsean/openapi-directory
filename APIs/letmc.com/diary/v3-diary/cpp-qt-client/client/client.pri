QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdvertisingBranchModel.h \
    $${PWD}/OAIAdvertisingBranchModelResults.h \
    $${PWD}/OAIBaseHypermediaLink.h \
    $${PWD}/OAIDiaryAppointmentDetails.h \
    $${PWD}/OAIDiaryAppointmentModel.h \
    $${PWD}/OAIDiaryAppointmentModelResults.h \
    $${PWD}/OAIDiaryAppointmentTypeModel.h \
    $${PWD}/OAIDiaryAppointmentTypeModelResults.h \
    $${PWD}/OAIDiaryBookingModel.h \
    $${PWD}/OAIDiaryGuestDetails.h \
    $${PWD}/OAIFeedbackSubmissionModel.h \
    $${PWD}/OAIGuestDiaryParametersModel.h \
    $${PWD}/OAIGuestDiaryParametersResultsModel.h \
    $${PWD}/OAILatestTenancyModel.h \
    $${PWD}/OAILinkedGuestModel.h \
    $${PWD}/OAILinkedLandlordModel.h \
    $${PWD}/OAILinkedPropertiesModel.h \
    $${PWD}/OAILinkedTenantModel.h \
# APIs
    $${PWD}/OAICompanyControllerApi.h \
    $${PWD}/OAIDiaryControllerApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIAdvertisingBranchModel.cpp \
    $${PWD}/OAIAdvertisingBranchModelResults.cpp \
    $${PWD}/OAIBaseHypermediaLink.cpp \
    $${PWD}/OAIDiaryAppointmentDetails.cpp \
    $${PWD}/OAIDiaryAppointmentModel.cpp \
    $${PWD}/OAIDiaryAppointmentModelResults.cpp \
    $${PWD}/OAIDiaryAppointmentTypeModel.cpp \
    $${PWD}/OAIDiaryAppointmentTypeModelResults.cpp \
    $${PWD}/OAIDiaryBookingModel.cpp \
    $${PWD}/OAIDiaryGuestDetails.cpp \
    $${PWD}/OAIFeedbackSubmissionModel.cpp \
    $${PWD}/OAIGuestDiaryParametersModel.cpp \
    $${PWD}/OAIGuestDiaryParametersResultsModel.cpp \
    $${PWD}/OAILatestTenancyModel.cpp \
    $${PWD}/OAILinkedGuestModel.cpp \
    $${PWD}/OAILinkedLandlordModel.cpp \
    $${PWD}/OAILinkedPropertiesModel.cpp \
    $${PWD}/OAILinkedTenantModel.cpp \
# APIs
    $${PWD}/OAICompanyControllerApi.cpp \
    $${PWD}/OAIDiaryControllerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
