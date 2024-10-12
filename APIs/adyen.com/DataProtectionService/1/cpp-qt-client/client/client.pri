QT += network

HEADERS += \
# Models
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAISubjectErasureByPspReferenceRequest.h \
    $${PWD}/OAISubjectErasureResponse.h \
# APIs
    $${PWD}/OAIGeneralApi.h \
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
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAISubjectErasureByPspReferenceRequest.cpp \
    $${PWD}/OAISubjectErasureResponse.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
