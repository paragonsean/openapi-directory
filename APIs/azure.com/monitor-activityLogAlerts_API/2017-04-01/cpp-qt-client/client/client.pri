QT += network

HEADERS += \
# Models
    $${PWD}/OAIActivityLogAlert.h \
    $${PWD}/OAIActivityLogAlertActionGroup.h \
    $${PWD}/OAIActivityLogAlertActionList.h \
    $${PWD}/OAIActivityLogAlertAllOfCondition.h \
    $${PWD}/OAIActivityLogAlertLeafCondition.h \
    $${PWD}/OAIActivityLogAlertList.h \
    $${PWD}/OAIActivityLogAlertPatch.h \
    $${PWD}/OAIActivityLogAlertPatchBody.h \
    $${PWD}/OAIActivityLogAlertResource.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIActivityLogAlert.cpp \
    $${PWD}/OAIActivityLogAlertActionGroup.cpp \
    $${PWD}/OAIActivityLogAlertActionList.cpp \
    $${PWD}/OAIActivityLogAlertAllOfCondition.cpp \
    $${PWD}/OAIActivityLogAlertLeafCondition.cpp \
    $${PWD}/OAIActivityLogAlertList.cpp \
    $${PWD}/OAIActivityLogAlertPatch.cpp \
    $${PWD}/OAIActivityLogAlertPatchBody.cpp \
    $${PWD}/OAIActivityLogAlertResource.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
