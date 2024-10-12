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

#include "OAIRange_over_Players.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRange_over_Players::OAIRange_over_Players(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRange_over_Players::OAIRange_over_Players() {
    this->initializeModel();
}

OAIRange_over_Players::~OAIRange_over_Players() {}

void OAIRange_over_Players::initializeModel() {

    m_birth_year_isSet = false;
    m_birth_year_isValid = false;

    m_birthday_isSet = false;
    m_birthday_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_hometown_isSet = false;
    m_hometown_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_nationality_isSet = false;
    m_nationality_isValid = false;

    m_role_isSet = false;
    m_role_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;
}

void OAIRange_over_Players::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRange_over_Players::fromJsonObject(QJsonObject json) {

    m_birth_year_isValid = ::OpenAPI::fromJsonValue(m_birth_year, json[QString("birth_year")]);
    m_birth_year_isSet = !json[QString("birth_year")].isNull() && m_birth_year_isValid;

    m_birthday_isValid = ::OpenAPI::fromJsonValue(m_birthday, json[QString("birthday")]);
    m_birthday_isSet = !json[QString("birthday")].isNull() && m_birthday_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_hometown_isValid = ::OpenAPI::fromJsonValue(m_hometown, json[QString("hometown")]);
    m_hometown_isSet = !json[QString("hometown")].isNull() && m_hometown_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_nationality_isValid = ::OpenAPI::fromJsonValue(m_nationality, json[QString("nationality")]);
    m_nationality_isSet = !json[QString("nationality")].isNull() && m_nationality_isValid;

    m_role_isValid = ::OpenAPI::fromJsonValue(m_role, json[QString("role")]);
    m_role_isSet = !json[QString("role")].isNull() && m_role_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;
}

QString OAIRange_over_Players::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRange_over_Players::asJsonObject() const {
    QJsonObject obj;
    if (m_birth_year.size() > 0) {
        obj.insert(QString("birth_year"), ::OpenAPI::toJsonValue(m_birth_year));
    }
    if (m_birthday.size() > 0) {
        obj.insert(QString("birthday"), ::OpenAPI::toJsonValue(m_birthday));
    }
    if (m_first_name.size() > 0) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_hometown.size() > 0) {
        obj.insert(QString("hometown"), ::OpenAPI::toJsonValue(m_hometown));
    }
    if (m_id.size() > 0) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_name.size() > 0) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_name.size() > 0) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_nationality.size() > 0) {
        obj.insert(QString("nationality"), ::OpenAPI::toJsonValue(m_nationality));
    }
    if (m_role.size() > 0) {
        obj.insert(QString("role"), ::OpenAPI::toJsonValue(m_role));
    }
    if (m_slug.size() > 0) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
    }
    return obj;
}

QList<double> OAIRange_over_Players::getBirthYear() const {
    return m_birth_year;
}
void OAIRange_over_Players::setBirthYear(const QList<double> &birth_year) {
    m_birth_year = birth_year;
    m_birth_year_isSet = true;
}

bool OAIRange_over_Players::is_birth_year_Set() const{
    return m_birth_year_isSet;
}

bool OAIRange_over_Players::is_birth_year_Valid() const{
    return m_birth_year_isValid;
}

QList<QString> OAIRange_over_Players::getBirthday() const {
    return m_birthday;
}
void OAIRange_over_Players::setBirthday(const QList<QString> &birthday) {
    m_birthday = birthday;
    m_birthday_isSet = true;
}

bool OAIRange_over_Players::is_birthday_Set() const{
    return m_birthday_isSet;
}

bool OAIRange_over_Players::is_birthday_Valid() const{
    return m_birthday_isValid;
}

QList<QString> OAIRange_over_Players::getFirstName() const {
    return m_first_name;
}
void OAIRange_over_Players::setFirstName(const QList<QString> &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIRange_over_Players::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIRange_over_Players::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QList<QString> OAIRange_over_Players::getHometown() const {
    return m_hometown;
}
void OAIRange_over_Players::setHometown(const QList<QString> &hometown) {
    m_hometown = hometown;
    m_hometown_isSet = true;
}

bool OAIRange_over_Players::is_hometown_Set() const{
    return m_hometown_isSet;
}

bool OAIRange_over_Players::is_hometown_Valid() const{
    return m_hometown_isValid;
}

QList<qint32> OAIRange_over_Players::getId() const {
    return m_id;
}
void OAIRange_over_Players::setId(const QList<qint32> &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRange_over_Players::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRange_over_Players::is_id_Valid() const{
    return m_id_isValid;
}

QList<QString> OAIRange_over_Players::getLastName() const {
    return m_last_name;
}
void OAIRange_over_Players::setLastName(const QList<QString> &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIRange_over_Players::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIRange_over_Players::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QList<QString> OAIRange_over_Players::getName() const {
    return m_name;
}
void OAIRange_over_Players::setName(const QList<QString> &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIRange_over_Players::is_name_Set() const{
    return m_name_isSet;
}

bool OAIRange_over_Players::is_name_Valid() const{
    return m_name_isValid;
}

QList<QString> OAIRange_over_Players::getNationality() const {
    return m_nationality;
}
void OAIRange_over_Players::setNationality(const QList<QString> &nationality) {
    m_nationality = nationality;
    m_nationality_isSet = true;
}

bool OAIRange_over_Players::is_nationality_Set() const{
    return m_nationality_isSet;
}

bool OAIRange_over_Players::is_nationality_Valid() const{
    return m_nationality_isValid;
}

QList<QString> OAIRange_over_Players::getRole() const {
    return m_role;
}
void OAIRange_over_Players::setRole(const QList<QString> &role) {
    m_role = role;
    m_role_isSet = true;
}

bool OAIRange_over_Players::is_role_Set() const{
    return m_role_isSet;
}

bool OAIRange_over_Players::is_role_Valid() const{
    return m_role_isValid;
}

QList<QString> OAIRange_over_Players::getSlug() const {
    return m_slug;
}
void OAIRange_over_Players::setSlug(const QList<QString> &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAIRange_over_Players::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAIRange_over_Players::is_slug_Valid() const{
    return m_slug_isValid;
}

bool OAIRange_over_Players::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_birth_year.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_birthday.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_hometown.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_nationality.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_role.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRange_over_Players::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
