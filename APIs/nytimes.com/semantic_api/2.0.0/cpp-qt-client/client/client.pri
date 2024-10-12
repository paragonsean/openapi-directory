QT += network

HEADERS += \
# Models
    $${PWD}/OAIConcept.h \
    $${PWD}/OAIConceptRelation.h \
    $${PWD}/OAIConcept_article_list.h \
    $${PWD}/OAIConcept_article_list_results_inner.h \
    $${PWD}/OAIConcept_article_list_results_inner_concepts.h \
    $${PWD}/OAIConcept_combinations_inner.h \
    $${PWD}/OAIConcept_links_inner.h \
    $${PWD}/OAIConcept_scope_notes_inner.h \
    $${PWD}/OAIConcept_taxonomy_inner.h \
    $${PWD}/OAI_name__concept_type___specific_concept__json_get_200_response.h \
    $${PWD}/OAI_search_json_get_200_response.h \
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
    $${PWD}/OAIConcept.cpp \
    $${PWD}/OAIConceptRelation.cpp \
    $${PWD}/OAIConcept_article_list.cpp \
    $${PWD}/OAIConcept_article_list_results_inner.cpp \
    $${PWD}/OAIConcept_article_list_results_inner_concepts.cpp \
    $${PWD}/OAIConcept_combinations_inner.cpp \
    $${PWD}/OAIConcept_links_inner.cpp \
    $${PWD}/OAIConcept_scope_notes_inner.cpp \
    $${PWD}/OAIConcept_taxonomy_inner.cpp \
    $${PWD}/OAI_name__concept_type___specific_concept__json_get_200_response.cpp \
    $${PWD}/OAI_search_json_get_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
