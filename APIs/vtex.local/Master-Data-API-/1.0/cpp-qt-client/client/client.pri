QT += network

HEADERS += \
# Models
    $${PWD}/OAIArEVentilaO.h \
    $${PWD}/OAICreateUpdateAddressRequests.h \
    $${PWD}/OAICreateUpdateProfileRequests.h \
    $${PWD}/OAIDEPRECATED_DocumentRequest.h \
    $${PWD}/OAIDepartmentVisitedTag.h \
    $${PWD}/OAIDocument.h \
    $${PWD}/OAIDocumentResponse.h \
    $${PWD}/OAIGetversion.h \
    $${PWD}/OAIListversion.h \
    $${PWD}/OAIName.h \
    $${PWD}/OAIProperties.h \
    $${PWD}/OAIPutindicesRequest.h \
    $${PWD}/OAISaveschemabynameRequest.h \
    $${PWD}/OAIScores.h \
    $${PWD}/OAIUsing_fields_all.h \
    $${PWD}/OAIValidatedocumentbyclustersRequest.h \
# APIs
    $${PWD}/OAIAddressesApi.h \
    $${PWD}/OAIClustersApi.h \
    $${PWD}/OAICustomerProfilesApi.h \
    $${PWD}/OAIDocumentsApi.h \
    $${PWD}/OAIIndicesApi.h \
    $${PWD}/OAISchemasApi.h \
    $${PWD}/OAIScrollApi.h \
    $${PWD}/OAISearchApi.h \
    $${PWD}/OAIVersionsApi.h \
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
    $${PWD}/OAIArEVentilaO.cpp \
    $${PWD}/OAICreateUpdateAddressRequests.cpp \
    $${PWD}/OAICreateUpdateProfileRequests.cpp \
    $${PWD}/OAIDEPRECATED_DocumentRequest.cpp \
    $${PWD}/OAIDepartmentVisitedTag.cpp \
    $${PWD}/OAIDocument.cpp \
    $${PWD}/OAIDocumentResponse.cpp \
    $${PWD}/OAIGetversion.cpp \
    $${PWD}/OAIListversion.cpp \
    $${PWD}/OAIName.cpp \
    $${PWD}/OAIProperties.cpp \
    $${PWD}/OAIPutindicesRequest.cpp \
    $${PWD}/OAISaveschemabynameRequest.cpp \
    $${PWD}/OAIScores.cpp \
    $${PWD}/OAIUsing_fields_all.cpp \
    $${PWD}/OAIValidatedocumentbyclustersRequest.cpp \
# APIs
    $${PWD}/OAIAddressesApi.cpp \
    $${PWD}/OAIClustersApi.cpp \
    $${PWD}/OAICustomerProfilesApi.cpp \
    $${PWD}/OAIDocumentsApi.cpp \
    $${PWD}/OAIIndicesApi.cpp \
    $${PWD}/OAISchemasApi.cpp \
    $${PWD}/OAIScrollApi.cpp \
    $${PWD}/OAISearchApi.cpp \
    $${PWD}/OAIVersionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
