/**
 * CS:GO v3 Stats
 * CS:GO v3 Stats
 *
 * The version of the OpenAPI document: 1.0
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
