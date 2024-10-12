QT += network

HEADERS += \
# Models
    $${PWD}/OAIDataset.h \
    $${PWD}/OAIFacet.h \
    $${PWD}/OAIInvestigation.h \
    $${PWD}/OAISolrQuery.h \
    $${PWD}/OAISolrResponse.h \
    $${PWD}/OAISolrResponse_response.h \
    $${PWD}/OAISolrResponse_responseHeader.h \
    $${PWD}/OAISolrquery_post_request.h \
    $${PWD}/OAISolrquery_post_request_params.h \
    $${PWD}/OAISubstance.h \
    $${PWD}/OAISubstanceComposition.h \
    $${PWD}/OAISubstanceStudy.h \
    $${PWD}/OAISubstanceStudySummary.h \
# APIs
    $${PWD}/OAIFacetsApi.h \
    $${PWD}/OAISearchApi.h \
    $${PWD}/OAIStructuresApi.h \
    $${PWD}/OAIStudiesApi.h \
    $${PWD}/OAISubstancesApi.h \
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
    $${PWD}/OAIDataset.cpp \
    $${PWD}/OAIFacet.cpp \
    $${PWD}/OAIInvestigation.cpp \
    $${PWD}/OAISolrQuery.cpp \
    $${PWD}/OAISolrResponse.cpp \
    $${PWD}/OAISolrResponse_response.cpp \
    $${PWD}/OAISolrResponse_responseHeader.cpp \
    $${PWD}/OAISolrquery_post_request.cpp \
    $${PWD}/OAISolrquery_post_request_params.cpp \
    $${PWD}/OAISubstance.cpp \
    $${PWD}/OAISubstanceComposition.cpp \
    $${PWD}/OAISubstanceStudy.cpp \
    $${PWD}/OAISubstanceStudySummary.cpp \
# APIs
    $${PWD}/OAIFacetsApi.cpp \
    $${PWD}/OAISearchApi.cpp \
    $${PWD}/OAIStructuresApi.cpp \
    $${PWD}/OAIStudiesApi.cpp \
    $${PWD}/OAISubstancesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
