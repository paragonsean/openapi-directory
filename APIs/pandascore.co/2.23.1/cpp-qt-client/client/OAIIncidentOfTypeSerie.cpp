/**
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIncidentOfTypeSerie.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIncidentOfTypeSerie::OAIIncidentOfTypeSerie(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIncidentOfTypeSerie::OAIIncidentOfTypeSerie() {
    this->initializeModel();
}

OAIIncidentOfTypeSerie::~OAIIncidentOfTypeSerie() {}

void OAIIncidentOfTypeSerie::initializeModel() {

    m_change_type_isSet = false;
    m_change_type_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_modified_at_isSet = false;
    m_modified_at_isValid = false;

    m_object_isSet = false;
    m_object_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIIncidentOfTypeSerie::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIncidentOfTypeSerie::fromJsonObject(QJsonObject json) {

    m_change_type_isValid = ::OpenAPI::fromJsonValue(m_change_type, json[QString("change_type")]);
    m_change_type_isSet = !json[QString("change_type")].isNull() && m_change_type_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_modified_at_isValid = ::OpenAPI::fromJsonValue(m_modified_at, json[QString("modified_at")]);
    m_modified_at_isSet = !json[QString("modified_at")].isNull() && m_modified_at_isValid;

    m_object_isValid = ::OpenAPI::fromJsonValue(m_object, json[QString("object")]);
    m_object_isSet = !json[QString("object")].isNull() && m_object_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIIncidentOfTypeSerie::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIncidentOfTypeSerie::asJsonObject() const {
    QJsonObject obj;
    if (m_change_type.isSet()) {
        obj.insert(QString("change_type"), ::OpenAPI::toJsonValue(m_change_type));
    }
    if (m_id.isSet()) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_modified_at_isSet) {
        obj.insert(QString("modified_at"), ::OpenAPI::toJsonValue(m_modified_at));
    }
    if (m_object.isSet()) {
        obj.insert(QString("object"), ::OpenAPI::toJsonValue(m_object));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIIncidentChangeType OAIIncidentOfTypeSerie::getChangeType() const {
    return m_change_type;
}
void OAIIncidentOfTypeSerie::setChangeType(const OAIIncidentChangeType &change_type) {
    m_change_type = change_type;
    m_change_type_isSet = true;
}

bool OAIIncidentOfTypeSerie::is_change_type_Set() const{
    return m_change_type_isSet;
}

bool OAIIncidentOfTypeSerie::is_change_type_Valid() const{
    return m_change_type_isValid;
}

OAIIncidentID OAIIncidentOfTypeSerie::getId() const {
    return m_id;
}
void OAIIncidentOfTypeSerie::setId(const OAIIncidentID &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIIncidentOfTypeSerie::is_id_Set() const{
    return m_id_isSet;
}

bool OAIIncidentOfTypeSerie::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIIncidentOfTypeSerie::getModifiedAt() const {
    return m_modified_at;
}
void OAIIncidentOfTypeSerie::setModifiedAt(const QDateTime &modified_at) {
    m_modified_at = modified_at;
    m_modified_at_isSet = true;
}

bool OAIIncidentOfTypeSerie::is_modified_at_Set() const{
    return m_modified_at_isSet;
}

bool OAIIncidentOfTypeSerie::is_modified_at_Valid() const{
    return m_modified_at_isValid;
}

OAISerie OAIIncidentOfTypeSerie::getObject() const {
    return m_object;
}
void OAIIncidentOfTypeSerie::setObject(const OAISerie &object) {
    m_object = object;
    m_object_isSet = true;
}

bool OAIIncidentOfTypeSerie::is_object_Set() const{
    return m_object_isSet;
}

bool OAIIncidentOfTypeSerie::is_object_Valid() const{
    return m_object_isValid;
}

QString OAIIncidentOfTypeSerie::getType() const {
    return m_type;
}
void OAIIncidentOfTypeSerie::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIIncidentOfTypeSerie::is_type_Set() const{
    return m_type_isSet;
}

bool OAIIncidentOfTypeSerie::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIIncidentOfTypeSerie::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_change_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_object.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIncidentOfTypeSerie::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_change_type_isValid && m_id_isValid && m_modified_at_isValid && m_object_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
