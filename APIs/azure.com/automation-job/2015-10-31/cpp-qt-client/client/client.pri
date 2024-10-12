QT += network

HEADERS += \
# Models
    $${PWD}/OAIJob.h \
    $${PWD}/OAIJobCreateParameters.h \
    $${PWD}/OAIJobCreateProperties.h \
    $${PWD}/OAIJobListResult.h \
    $${PWD}/OAIJobProperties.h \
    $${PWD}/OAIJobProvisioningStateProperty.h \
    $${PWD}/OAIJobStream.h \
    $${PWD}/OAIJobStreamListResult.h \
    $${PWD}/OAIJobStreamProperties.h \
    $${PWD}/OAIJob_ListByAutomationAccount_default_response.h \
    $${PWD}/OAIRunbookAssociationProperty.h \
    $${PWD}/OAIScheduleAssociationProperty.h \
# APIs
    $${PWD}/OAIJobApi.h \
    $${PWD}/OAIJobStreamApi.h \
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
    $${PWD}/OAIJob.cpp \
    $${PWD}/OAIJobCreateParameters.cpp \
    $${PWD}/OAIJobCreateProperties.cpp \
    $${PWD}/OAIJobListResult.cpp \
    $${PWD}/OAIJobProperties.cpp \
    $${PWD}/OAIJobProvisioningStateProperty.cpp \
    $${PWD}/OAIJobStream.cpp \
    $${PWD}/OAIJobStreamListResult.cpp \
    $${PWD}/OAIJobStreamProperties.cpp \
    $${PWD}/OAIJob_ListByAutomationAccount_default_response.cpp \
    $${PWD}/OAIRunbookAssociationProperty.cpp \
    $${PWD}/OAIScheduleAssociationProperty.cpp \
# APIs
    $${PWD}/OAIJobApi.cpp \
    $${PWD}/OAIJobStreamApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
