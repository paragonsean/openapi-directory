/**
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISearch_200_response.h
 *
 * 
 */

#ifndef OAISearch_200_response_H
#define OAISearch_200_response_H

#include <QJsonObject>

#include "OAISearch_200_response_grouped_search_result.h"
#include <QJsonValue>
#include <QList>
#include <QMap>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISearch_200_response : public OAIObject {
public:
    OAISearch_200_response();
    OAISearch_200_response(QString json);
    ~OAISearch_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QJsonValue> getCategories() const;
    void setCategories(const QList<QJsonValue> &categories);
    bool is_categories_Set() const;
    bool is_categories_Valid() const;

    OAISearch_200_response_grouped_search_result getGroupedSearchResult() const;
    void setGroupedSearchResult(const OAISearch_200_response_grouped_search_result &grouped_search_result);
    bool is_grouped_search_result_Set() const;
    bool is_grouped_search_result_Valid() const;

    QList<QJsonValue> getGroups() const;
    void setGroups(const QList<QJsonValue> &groups);
    bool is_groups_Set() const;
    bool is_groups_Valid() const;

    QList<QJsonValue> getPosts() const;
    void setPosts(const QList<QJsonValue> &posts);
    bool is_posts_Set() const;
    bool is_posts_Valid() const;

    QList<QJsonValue> getTags() const;
    void setTags(const QList<QJsonValue> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    QList<QJsonValue> getUsers() const;
    void setUsers(const QList<QJsonValue> &users);
    bool is_users_Set() const;
    bool is_users_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QJsonValue> m_categories;
    bool m_categories_isSet;
    bool m_categories_isValid;

    OAISearch_200_response_grouped_search_result m_grouped_search_result;
    bool m_grouped_search_result_isSet;
    bool m_grouped_search_result_isValid;

    QList<QJsonValue> m_groups;
    bool m_groups_isSet;
    bool m_groups_isValid;

    QList<QJsonValue> m_posts;
    bool m_posts_isSet;
    bool m_posts_isValid;

    QList<QJsonValue> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    QList<QJsonValue> m_users;
    bool m_users_isSet;
    bool m_users_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISearch_200_response)

#endif // OAISearch_200_response_H
