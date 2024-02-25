//
//  LoginViewModel.swift
//  SPLITWISE
//
//  Created by Irfan on 24/02/24.
//

import SwiftUI
import Firebase


class LoginViewModel: ObservableObject {
    
    @Published var mobileNO:String = ""
    @Published var otpCode:String = ""
    
    @Published var CLIENT_CODE:String = ""
    @Published var showOTPField: Bool = false
    
    
    @Published var showError: Bool = false
    @Published var errorMessage: String = ""
    
    
    //Firebase API's
    
    func getOTPCode(){
        UIApplication.shared.closeKeyboard()
        Task{
            do{
                Auth.auth().settings?.isAppVerificationDisabledForTesting = true
                let  code = try await PhoneAuthProvider.provider().verifyPhoneNumber("+\(mobileNO)", uiDelegate: nil)
                await MainActor.run(body: {
                    CLIENT_CODE = code
                    
                    withAnimation(.easeInOut){showOTPField = true}
                })
                
                
            }catch{
                await handleError(error: error)
                
            }
        }
        
        
    }
    
    func verifyOTPCode(){
        UIApplication.shared.closeKeyboard()
        
        Task{
            do{
                let credential = PhoneAuthProvider.provider().credential(withVerificationID: CLIENT_CODE, verificationCode: otpCode)
                try await Auth.auth().signIn(with: credential)
                
                print("Success!!")
                
            }catch{
                await handleError(error: error)
            }
        }
        
    }
    
    
    //Handlign Error
    
    func handleError(error: Error)async{
        await MainActor.run(body: {
            errorMessage = error.localizedDescription
            showError.toggle()
        })
    }
    
    
}


extension UIApplication{
    func closeKeyboard(){
        sendAction(#selector(UIResponder.resignFirstResponder), to: nil, from: nil, for: nil)
    }
}
