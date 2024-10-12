QT += network

HEADERS += \
# Models
    $${PWD}/OAIStep.h \
    $${PWD}/OAIUpdateRun.h \
    $${PWD}/OAIUpdateRunList.h \
    $${PWD}/OAIUpdateRunModel.h \
    $${PWD}/OAIUpdateRunState.h \
# APIs
    $${PWD}/OAIUpdateRunsApi.h \
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
    $${PWD}/OAIStep.cpp \
    $${PWD}/OAIUpdateRun.cpp \
    $${PWD}/OAIUpdateRunList.cpp \
    $${PWD}/OAIUpdateRunModel.cpp \
    $${PWD}/OAIUpdateRunState.cpp \
# APIs
    $${PWD}/OAIUpdateRunsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
