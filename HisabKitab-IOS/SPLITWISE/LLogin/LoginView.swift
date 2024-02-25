//
//  LoginView.swift
//  SPLITWISE
//
//  Created by Irfan on 24/02/24.
//

import SwiftUI

struct LoginView: View {
    @StateObject var loginModel: LoginViewModel = .init()
   
    
    var body: some View {
        ZStack{
            Color.blue.opacity(0.1).ignoresSafeArea()
            ScrollView(.vertical, showsIndicators: false){
                VStack(alignment: .leading, spacing:15){
                    Spacer()
                    Image(systemName:"person")
                        .font(.system(size:68)).foregroundColor(.indigo)
                    
                    (Text("Welcome,").foregroundColor(.black)+Text("\nLogin to Continue").foregroundColor(.gray)).font(.title).fontWeight(.semibold).lineSpacing(10).padding(.top,20).padding(.trailing,15)
                    
                    CustomTextField(hint: "+91 1234567", text: $loginModel.mobileNO).disabled(loginModel.showOTPField).opacity(loginModel.showOTPField ? 0.4 : 1).padding(.top,50)
                    
                    CustomTextField(hint: "OTP", text: $loginModel.otpCode).disabled(loginModel.showOTPField).opacity(loginModel.showOTPField ? 0.4 : 1).padding(.top,20)
                    
                    Button(action: loginModel.showOTPField ? loginModel.verifyOTPCode :   loginModel.getOTPCode)
                    {
                        HStack(spacing:15){
                            Text(loginModel.showOTPField ? "Verify Code" : "Get Code").fontWeight(.semibold).contentTransition(.identity)
                            Image(systemName: "line.diagonal.arrow").font(.title).rotationEffect(.init(degrees: 45))
                            
                        }.padding(.horizontal,25).padding(.vertical).background{
                            RoundedRectangle(cornerRadius: 15, style: .continuous).fill(.black.opacity(0.89))
                        }
                    }.padding(.top,27)
                    
                    
                    
                }.padding(.leading,60).padding(.vertical,15)
            }
            .alert(loginModel.errorMessage, isPresented: $loginModel.showError){
            }
        }
        
    }
}

#Preview {
    LoginView()
}
