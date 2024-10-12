QT += network

HEADERS += \
# Models
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAILongRunningRecognizeMetadata.h \
    $${PWD}/OAILongRunningRecognizeResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAISpeechRecognitionAlternative.h \
    $${PWD}/OAISpeechRecognitionResult.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIWordInfo.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAILongRunningRecognizeMetadata.cpp \
    $${PWD}/OAILongRunningRecognizeResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAISpeechRecognitionAlternative.cpp \
    $${PWD}/OAISpeechRecognitionResult.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIWordInfo.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
