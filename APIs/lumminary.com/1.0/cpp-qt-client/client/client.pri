QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessScope.h \
    $${PWD}/OAIAuthorization.h \
    $${PWD}/OAIClientGene.h \
    $${PWD}/OAIClientSNP.h \
    $${PWD}/OAICustomerAddress.h \
    $${PWD}/OAICustomerName.h \
    $${PWD}/OAIFileLocation.h \
    $${PWD}/OAIJavascriptWebToken.h \
    $${PWD}/OAIMolecularLocation.h \
    $${PWD}/OAIProduct.h \
    $${PWD}/OAIPublicGene.h \
    $${PWD}/OAIPublicSNP.h \
    $${PWD}/OAIReferenceChromosomeOverview.h \
    $${PWD}/OAIReferenceGenomeOverview.h \
    $${PWD}/OAIReferenceSequence.h \
    $${PWD}/OAIReportCredentials.h \
    $${PWD}/OAIReportFile.h \
    $${PWD}/OAISnpsMinRequired.h \
# APIs
    $${PWD}/OAILumminaryAPISpecApi.h \
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
    $${PWD}/OAIAccessScope.cpp \
    $${PWD}/OAIAuthorization.cpp \
    $${PWD}/OAIClientGene.cpp \
    $${PWD}/OAIClientSNP.cpp \
    $${PWD}/OAICustomerAddress.cpp \
    $${PWD}/OAICustomerName.cpp \
    $${PWD}/OAIFileLocation.cpp \
    $${PWD}/OAIJavascriptWebToken.cpp \
    $${PWD}/OAIMolecularLocation.cpp \
    $${PWD}/OAIProduct.cpp \
    $${PWD}/OAIPublicGene.cpp \
    $${PWD}/OAIPublicSNP.cpp \
    $${PWD}/OAIReferenceChromosomeOverview.cpp \
    $${PWD}/OAIReferenceGenomeOverview.cpp \
    $${PWD}/OAIReferenceSequence.cpp \
    $${PWD}/OAIReportCredentials.cpp \
    $${PWD}/OAIReportFile.cpp \
    $${PWD}/OAISnpsMinRequired.cpp \
# APIs
    $${PWD}/OAILumminaryAPISpecApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
