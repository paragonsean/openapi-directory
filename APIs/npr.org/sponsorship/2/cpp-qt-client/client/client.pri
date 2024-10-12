QT += network

HEADERS += \
# Models
    $${PWD}/OAIAbstractCDocLink.h \
    $${PWD}/OAIAbstractLink.h \
    $${PWD}/OAIAdTrackingData.h \
    $${PWD}/OAIAdTrackingDocument.h \
    $${PWD}/OAIAdXml.h \
    $${PWD}/OAIAffiliation.h \
    $${PWD}/OAICollectionDocument.h \
    $${PWD}/OAICompanionXml.h \
    $${PWD}/OAICreativeXml.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDocument.h \
    $${PWD}/OAIErrorXmlDocument.h \
    $${PWD}/OAIInLineXml.h \
    $${PWD}/OAILinearXml.h \
    $${PWD}/OAIUserAdData.h \
    $${PWD}/OAIUserAdDocument.h \
    $${PWD}/OAIVASTXml.h \
# APIs
    $${PWD}/OAISponsorshipApi.h \
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
    $${PWD}/OAIAbstractCDocLink.cpp \
    $${PWD}/OAIAbstractLink.cpp \
    $${PWD}/OAIAdTrackingData.cpp \
    $${PWD}/OAIAdTrackingDocument.cpp \
    $${PWD}/OAIAdXml.cpp \
    $${PWD}/OAIAffiliation.cpp \
    $${PWD}/OAICollectionDocument.cpp \
    $${PWD}/OAICompanionXml.cpp \
    $${PWD}/OAICreativeXml.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDocument.cpp \
    $${PWD}/OAIErrorXmlDocument.cpp \
    $${PWD}/OAIInLineXml.cpp \
    $${PWD}/OAILinearXml.cpp \
    $${PWD}/OAIUserAdData.cpp \
    $${PWD}/OAIUserAdDocument.cpp \
    $${PWD}/OAIVASTXml.cpp \
# APIs
    $${PWD}/OAISponsorshipApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
