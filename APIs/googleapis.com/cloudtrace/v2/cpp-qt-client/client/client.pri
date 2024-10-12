QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnnotation.h \
    $${PWD}/OAIAttributeValue.h \
    $${PWD}/OAIAttributes.h \
    $${PWD}/OAIBatchWriteSpansRequest.h \
    $${PWD}/OAILink.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAIMessageEvent.h \
    $${PWD}/OAIModule.h \
    $${PWD}/OAISpan.h \
    $${PWD}/OAIStackFrame.h \
    $${PWD}/OAIStackFrames.h \
    $${PWD}/OAIStackTrace.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITimeEvent.h \
    $${PWD}/OAITimeEvents.h \
    $${PWD}/OAITruncatableString.h \
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
    $${PWD}/OAIAnnotation.cpp \
    $${PWD}/OAIAttributeValue.cpp \
    $${PWD}/OAIAttributes.cpp \
    $${PWD}/OAIBatchWriteSpansRequest.cpp \
    $${PWD}/OAILink.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAIMessageEvent.cpp \
    $${PWD}/OAIModule.cpp \
    $${PWD}/OAISpan.cpp \
    $${PWD}/OAIStackFrame.cpp \
    $${PWD}/OAIStackFrames.cpp \
    $${PWD}/OAIStackTrace.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITimeEvent.cpp \
    $${PWD}/OAITimeEvents.cpp \
    $${PWD}/OAITruncatableString.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
