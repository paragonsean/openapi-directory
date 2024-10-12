QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnnotation.h \
    $${PWD}/OAIAnnotationError.h \
    $${PWD}/OAIAnnotationsListResult.h \
    $${PWD}/OAIInnerError.h \
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
    $${PWD}/OAIAnnotation.cpp \
    $${PWD}/OAIAnnotationError.cpp \
    $${PWD}/OAIAnnotationsListResult.cpp \
    $${PWD}/OAIInnerError.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
