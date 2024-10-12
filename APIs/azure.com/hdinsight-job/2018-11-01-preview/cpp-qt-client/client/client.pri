QT += network

HEADERS += \
# Models
    $${PWD}/OAIAppState.h \
    $${PWD}/OAIJobDetailRootJsonObject.h \
    $${PWD}/OAIJobID.h \
    $${PWD}/OAIJobListJsonObject.h \
    $${PWD}/OAIJobOperationsErrorResponse.h \
    $${PWD}/OAIJobSubmissionJsonResponse.h \
    $${PWD}/OAIProfile.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIUserargs.h \
# APIs
    $${PWD}/OAIJobApi.h \
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
    $${PWD}/OAIAppState.cpp \
    $${PWD}/OAIJobDetailRootJsonObject.cpp \
    $${PWD}/OAIJobID.cpp \
    $${PWD}/OAIJobListJsonObject.cpp \
    $${PWD}/OAIJobOperationsErrorResponse.cpp \
    $${PWD}/OAIJobSubmissionJsonResponse.cpp \
    $${PWD}/OAIProfile.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIUserargs.cpp \
# APIs
    $${PWD}/OAIJobApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
