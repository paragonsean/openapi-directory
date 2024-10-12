QT += network

HEADERS += \
# Models
    $${PWD}/OAIActionPlanAdminProperties.h \
    $${PWD}/OAIActionPlanAdminProperties_error.h \
    $${PWD}/OAIActionPlanAdminProperties_parameters.h \
    $${PWD}/OAIActionPlanList.h \
    $${PWD}/OAIActionPlanResourceEntity.h \
# APIs
    $${PWD}/OAIActionPlansApi.h \
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
    $${PWD}/OAIActionPlanAdminProperties.cpp \
    $${PWD}/OAIActionPlanAdminProperties_error.cpp \
    $${PWD}/OAIActionPlanAdminProperties_parameters.cpp \
    $${PWD}/OAIActionPlanList.cpp \
    $${PWD}/OAIActionPlanResourceEntity.cpp \
# APIs
    $${PWD}/OAIActionPlansApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
