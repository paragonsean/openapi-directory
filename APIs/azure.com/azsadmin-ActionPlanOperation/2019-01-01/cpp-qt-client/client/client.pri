QT += network

HEADERS += \
# Models
    $${PWD}/OAIActionPlanOperationAdminProperties.h \
    $${PWD}/OAIActionPlanOperationAdminProperties_error.h \
    $${PWD}/OAIActionPlanOperationResourceEntity.h \
    $${PWD}/OAIActionPlanOperationsList.h \
# APIs
    $${PWD}/OAIActionPlanOperationsApi.h \
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
    $${PWD}/OAIActionPlanOperationAdminProperties.cpp \
    $${PWD}/OAIActionPlanOperationAdminProperties_error.cpp \
    $${PWD}/OAIActionPlanOperationResourceEntity.cpp \
    $${PWD}/OAIActionPlanOperationsList.cpp \
# APIs
    $${PWD}/OAIActionPlanOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
