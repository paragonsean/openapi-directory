QT += network

HEADERS += \
# Models
    $${PWD}/OAIAcceptDisputeRequest.h \
    $${PWD}/OAIAcceptDisputeResponse.h \
    $${PWD}/OAIDefendDisputeRequest.h \
    $${PWD}/OAIDefendDisputeResponse.h \
    $${PWD}/OAIDefenseDocument.h \
    $${PWD}/OAIDefenseDocumentType.h \
    $${PWD}/OAIDefenseReason.h \
    $${PWD}/OAIDefenseReasonsRequest.h \
    $${PWD}/OAIDefenseReasonsResponse.h \
    $${PWD}/OAIDeleteDefenseDocumentRequest.h \
    $${PWD}/OAIDeleteDefenseDocumentResponse.h \
    $${PWD}/OAIDisputeServiceResult.h \
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAISupplyDefenseDocumentRequest.h \
    $${PWD}/OAISupplyDefenseDocumentResponse.h \
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
    $${PWD}/OAIAcceptDisputeRequest.cpp \
    $${PWD}/OAIAcceptDisputeResponse.cpp \
    $${PWD}/OAIDefendDisputeRequest.cpp \
    $${PWD}/OAIDefendDisputeResponse.cpp \
    $${PWD}/OAIDefenseDocument.cpp \
    $${PWD}/OAIDefenseDocumentType.cpp \
    $${PWD}/OAIDefenseReason.cpp \
    $${PWD}/OAIDefenseReasonsRequest.cpp \
    $${PWD}/OAIDefenseReasonsResponse.cpp \
    $${PWD}/OAIDeleteDefenseDocumentRequest.cpp \
    $${PWD}/OAIDeleteDefenseDocumentResponse.cpp \
    $${PWD}/OAIDisputeServiceResult.cpp \
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAISupplyDefenseDocumentRequest.cpp \
    $${PWD}/OAISupplyDefenseDocumentResponse.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
