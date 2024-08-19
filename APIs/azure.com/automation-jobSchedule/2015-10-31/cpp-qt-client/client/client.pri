QT += network

HEADERS += \
# Models
    $${PWD}/OAIJobSchedule.h \
    $${PWD}/OAIJobScheduleCreateParameters.h \
    $${PWD}/OAIJobScheduleCreateProperties.h \
    $${PWD}/OAIJobScheduleListResult.h \
    $${PWD}/OAIJobScheduleProperties.h \
    $${PWD}/OAIJobSchedule_ListByAutomationAccount_default_response.h \
    $${PWD}/OAIRunbookAssociationProperty.h \
    $${PWD}/OAIScheduleAssociationProperty.h \
# APIs
    $${PWD}/OAIJobScheduleApi.h \
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
    $${PWD}/OAIJobSchedule.cpp \
    $${PWD}/OAIJobScheduleCreateParameters.cpp \
    $${PWD}/OAIJobScheduleCreateProperties.cpp \
    $${PWD}/OAIJobScheduleListResult.cpp \
    $${PWD}/OAIJobScheduleProperties.cpp \
    $${PWD}/OAIJobSchedule_ListByAutomationAccount_default_response.cpp \
    $${PWD}/OAIRunbookAssociationProperty.cpp \
    $${PWD}/OAIScheduleAssociationProperty.cpp \
# APIs
    $${PWD}/OAIJobScheduleApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
