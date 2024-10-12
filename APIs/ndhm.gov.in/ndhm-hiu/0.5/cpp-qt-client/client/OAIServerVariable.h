/**
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * Representing a Server Variable for server URL template substitution.
 */
#ifndef OAI_SERVERVARIABLE_H
#define OAI_SERVERVARIABLE_H
#include <QString>
#include <QSet>

namespace OpenAPI {

class OAIServerVariable {
public:

    /**
     * @param description A description for the server variable.
     * @param defaultValue The default value to use for substitution.
     * @param enumValues An enumeration of string values to be used if the substitution options are from a limited set.
     */
    OAIServerVariable(const QString &description, const QString &defaultValue, const QSet<QString> &enumValues)
    : _defaultValue(defaultValue),
      _description(description),
      _enumValues(enumValues){}

    OAIServerVariable(){}
    ~OAIServerVariable(){}

    int setDefaultValue(const QString& value){
      if( _enumValues.contains(value)){
        _defaultValue = value;
        return 0;
      }
      return -2;
    }

    QString getDefaultValue(){return _defaultValue;}
    QSet<QString> getEnumValues(){return _enumValues;}


    QString _defaultValue;
    QString _description;
    QSet<QString> _enumValues;

};

} // namespace OpenAPI

#endif // OAI_SERVERVARIABLE_H
